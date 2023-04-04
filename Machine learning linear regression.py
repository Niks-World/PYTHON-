{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d0713682",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import linear_model\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.model_selection import train_test_split\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b24b8956",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ccadb57d",
   "metadata": {},
   "outputs": [],
   "source": [
    "customer_churn=pd.read_csv('D:\\customer_churn.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4e76e113",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>customerID</th>\n",
       "      <th>gender</th>\n",
       "      <th>SeniorCitizen</th>\n",
       "      <th>Partner</th>\n",
       "      <th>Dependents</th>\n",
       "      <th>tenure</th>\n",
       "      <th>PhoneService</th>\n",
       "      <th>MultipleLines</th>\n",
       "      <th>InternetService</th>\n",
       "      <th>OnlineSecurity</th>\n",
       "      <th>...</th>\n",
       "      <th>DeviceProtection</th>\n",
       "      <th>TechSupport</th>\n",
       "      <th>StreamingTV</th>\n",
       "      <th>StreamingMovies</th>\n",
       "      <th>Contract</th>\n",
       "      <th>PaperlessBilling</th>\n",
       "      <th>PaymentMethod</th>\n",
       "      <th>MonthlyCharges</th>\n",
       "      <th>TotalCharges</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7590-VHVEG</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>1</td>\n",
       "      <td>No</td>\n",
       "      <td>No phone service</td>\n",
       "      <td>DSL</td>\n",
       "      <td>No</td>\n",
       "      <td>...</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Month-to-month</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Electronic check</td>\n",
       "      <td>29.85</td>\n",
       "      <td>29.85</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5575-GNVDE</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>34</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>DSL</td>\n",
       "      <td>Yes</td>\n",
       "      <td>...</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>One year</td>\n",
       "      <td>No</td>\n",
       "      <td>Mailed check</td>\n",
       "      <td>56.95</td>\n",
       "      <td>1889.5</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3668-QPYBK</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>2</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>DSL</td>\n",
       "      <td>Yes</td>\n",
       "      <td>...</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Month-to-month</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Mailed check</td>\n",
       "      <td>53.85</td>\n",
       "      <td>108.15</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7795-CFOCW</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>45</td>\n",
       "      <td>No</td>\n",
       "      <td>No phone service</td>\n",
       "      <td>DSL</td>\n",
       "      <td>Yes</td>\n",
       "      <td>...</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>One year</td>\n",
       "      <td>No</td>\n",
       "      <td>Bank transfer (automatic)</td>\n",
       "      <td>42.30</td>\n",
       "      <td>1840.75</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>9237-HQITU</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>2</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Fiber optic</td>\n",
       "      <td>No</td>\n",
       "      <td>...</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Month-to-month</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Electronic check</td>\n",
       "      <td>70.70</td>\n",
       "      <td>151.65</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   customerID  gender  SeniorCitizen Partner Dependents  tenure PhoneService  \\\n",
       "0  7590-VHVEG  Female              0     Yes         No       1           No   \n",
       "1  5575-GNVDE    Male              0      No         No      34          Yes   \n",
       "2  3668-QPYBK    Male              0      No         No       2          Yes   \n",
       "3  7795-CFOCW    Male              0      No         No      45           No   \n",
       "4  9237-HQITU  Female              0      No         No       2          Yes   \n",
       "\n",
       "      MultipleLines InternetService OnlineSecurity  ... DeviceProtection  \\\n",
       "0  No phone service             DSL             No  ...               No   \n",
       "1                No             DSL            Yes  ...              Yes   \n",
       "2                No             DSL            Yes  ...               No   \n",
       "3  No phone service             DSL            Yes  ...              Yes   \n",
       "4                No     Fiber optic             No  ...               No   \n",
       "\n",
       "  TechSupport StreamingTV StreamingMovies        Contract PaperlessBilling  \\\n",
       "0          No          No              No  Month-to-month              Yes   \n",
       "1          No          No              No        One year               No   \n",
       "2          No          No              No  Month-to-month              Yes   \n",
       "3         Yes          No              No        One year               No   \n",
       "4          No          No              No  Month-to-month              Yes   \n",
       "\n",
       "               PaymentMethod MonthlyCharges  TotalCharges Churn  \n",
       "0           Electronic check          29.85         29.85    No  \n",
       "1               Mailed check          56.95        1889.5    No  \n",
       "2               Mailed check          53.85        108.15   Yes  \n",
       "3  Bank transfer (automatic)          42.30       1840.75    No  \n",
       "4           Electronic check          70.70        151.65   Yes  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "customer_churn.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "48750dd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "y=customer_churn[['MonthlyCharges']]\n",
    "x=customer_churn[['tenure']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7ca29117",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(   tenure\n",
       " 0       1\n",
       " 1      34\n",
       " 2       2\n",
       " 3      45\n",
       " 4       2,\n",
       "    MonthlyCharges\n",
       " 0           29.85\n",
       " 1           56.95\n",
       " 2           53.85\n",
       " 3           42.30\n",
       " 4           70.70)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.head(),y.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1d091ff6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#30% of the record to test set and rest to the training set \n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5b4a32bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((4930, 1), (4930, 1), (2113, 1), (2113, 1))"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape,x_train.shape,y_test.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "39102e22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regressor = LinearRegression()\n",
    "\n",
    "regressor.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4b6f953c",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=regressor.predict(x_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2056d010",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "29.394584027273893"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import mean_squared_error\n",
    "\n",
    "np.sqrt(mean_squared_error(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "711d9f2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([[60.95089608],\n",
       "        [72.98096699],\n",
       "        [59.1903979 ],\n",
       "        [55.66940154],\n",
       "        [71.51388517]]),\n",
       "       MonthlyCharges\n",
       " 2200           58.20\n",
       " 4627          116.60\n",
       " 3225           71.95\n",
       " 2828           20.45\n",
       " 3768           77.75)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#monthlyCharges predicted value\n",
    "y_pred=regressor.predict(x_test)\n",
    "y_pred[:5],y_test[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "e786df06",
   "metadata": {},
   "outputs": [],
   "source": [
    "customer_churn=pd.read_csv('D:\\customer_churn.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "6eba63f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "y=customer_churn[['MonthlyCharges']]\n",
    "x=customer_churn[['Churn']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "cf48f085",
   "metadata": {},
   "outputs": [],
   "source": [
    "#35% will be test set and 75% will train set\n",
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.35,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "b95a9a50",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  return f(*args, **kwargs)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "log_model = LogisticRegression()\n",
    "\n",
    "log_model.fit(y_train,x_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "dd321d21",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=log_model.predict(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "2f7dc12f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix,accuracy_score\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90c69a31",
   "metadata": {},
   "outputs": [],
   "source": [
    "confusion_matrix(y_test,y_pred),accuracy_score(y_test,y_pred)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
