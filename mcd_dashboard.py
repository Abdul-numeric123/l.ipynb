{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5b56affe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "475a78e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(page_title=\"McDonald's Financial Dashboard\", layout=\"wide\")\n",
    "\n",
    "csv_path = r\"C:\\Users\\DELL\\Downloads\\twitter.py\\McDonalds_Financial_Statements.csv\"\n",
    "df = pd.read_csv(csv_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a20edb36",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-02 00:37:55.034 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\DELL\\AppData\\Roaming\\Python\\Python312\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "st.title(\"📊 McDonald's Financial Dashboard\")\n",
    "\n",
    "if st.checkbox(\"Show Raw Data\"):\n",
    "    st.write(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "327214f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.subheader(\"🔍 Summary Statistics\")\n",
    "st.write(df.describe())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "843bbfc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-02 00:38:02.500 Session state does not function when running a script without `streamlit run`\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numeric_cols = df.select_dtypes(include='number').columns.tolist()\n",
    "selected_col = st.selectbox(\"Select a numeric column to plot\", numeric_cols)\n",
    "\n",
    "st.subheader(f\"📈 Trend of {selected_col}\")\n",
    "fig, ax = plt.subplots()\n",
    "sns.lineplot(data=df, x=df.columns[0], y=selected_col, ax=ax)  # Assuming 1st column is Date/Period\n",
    "plt.xticks(rotation=45)\n",
    "st.pyplot(fig)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c359c657",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.subheader(\"🔗 Correlation Heatmap\")\n",
    "fig2, ax2 = plt.subplots()\n",
    "sns.heatmap(df[numeric_cols].corr(), annot=True, cmap=\"coolwarm\", ax=ax2)\n",
    "st.pyplot(fig2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ebb19550",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3945078060.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[9], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run mcd_dashboard.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run mcd_dashboard.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2f17fb0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function dir>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6194a642",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3945078060.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[22], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run mcd_dashboard.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run mcd_dashboard.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "102d5dd7",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3945078060.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[23], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run mcd_dashboard.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run mcd_dashboard.py\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
