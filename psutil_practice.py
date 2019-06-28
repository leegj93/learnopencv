{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/leegj93/learnopencv/blob/master/psutil_practice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tLmtvb9gE9b4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 221
        },
        "outputId": "dae3cbba-84e8-4a5c-e4dc-1aeaa2cbe1ee"
      },
      "source": [
        "import psutil\n",
        "import datetime, time\n",
        "import signal\n",
        "import sys\n",
        "import csv\n",
        "import os\n",
        "\n",
        "class bcolors:\n",
        "  HEADER = '\\033[95m'\n",
        "  OKBLUE = '\\033[94m'\n",
        "  OKGREEN = '\\033[92m'\n",
        "  WARNING = '\\033[93m'\n",
        "  FAIL = '\\033[91m'\n",
        "  ENDC = '\\033[0m'\n",
        "  BOLD = '\\033[1m'\n",
        "  UNDERLINE = '\\033[4m'\n",
        "\n",
        "  \n",
        "  \n",
        "class ngle_util:\n",
        "  def _init_(self):\n",
        "    pass\n",
        "  \n",
        "  def signal_handler(self, signal, frame):\n",
        "    print('Lose nGle Sys Mon')\n",
        "    sys.exit(0)\n",
        "  def change_B_to_k(self, ebyte):\n",
        "    return int(ebyte/1024)\n",
        "  def change_B_to_M(self,ebyte):\n",
        "    return int((ebyte/1024)/1024)\n",
        "  \n",
        "  def change_color(self, comm):\n",
        "    if 80.0 <= comm <= 100.0:\n",
        "      strComm = bcolors.FAIL + str(comm) + \"%\" + bcolors.ENDC\n",
        "    elif 70.0 <= comm <= 79.0:\n",
        "      strComm = bcolors.WARNING + str(comm) + \"%\" + bcolors.ENDC\n",
        "    else:\n",
        "      strComm = str(comm) + \"%\"\n",
        "    return strComm\n",
        "  \n",
        "  def get_date(self, date_when='today'):\n",
        "    today = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')\n",
        "    \n",
        "    if date_when == \"today\":\n",
        "      date = today\n",
        "    else:\n",
        "      date = today\n",
        "    \n",
        "    return date\n",
        "\n",
        "      "
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-10-6adafd268f05>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mdate\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 50\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtoday\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     51\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'today' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Wgvt9g08Jqaj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}