�
    �f�f!  �                   ��  � d dl Z d dlZd dlZd dlmZ d dlmZ i dd�dd�dd	�d
d�de�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d�d$d%i�Zd&ed'e	e
ee�                  fd(�Zd&ed'efd)�Zd&ed*ed'efd+�Zd,e
d-efd.�Z ed/�  �          ed0�  �        Z eed1�  �        5 Z e	 ed2� e�                    �   �         �  �        �  �        Zddd�  �         n# 1 swxY w Y    e ed3�  �        �  �        Z ed4� eD �   �         �  �        Z ee�  �        Z ed5d6�  �        5 Ze�                    d7�  �         ddd�  �         n# 1 swxY w Y    ee�  �        D ]nZe�                    �   �         Ze�                    �   �         Z eD ]AZ! ej"        ee! ee e!d8         �  �        f�9�  �        Z#d:e#_$        e#�%                    �   �          �B�o ed;�  �          ed<�  �         dS )=�    N)�deque)�findall�	authorityzwww.facebook.com�Acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7zAccept-Language�vizCache-Controlz	max-age=0�Cookie�Dpr�1z	Sec-Ch-Uaz@"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"zSec-Ch-Ua-Full-Version-Listz\"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"zSec-Ch-Ua-Mobilez?0zSec-Ch-Ua-Modelz""zSec-Ch-Ua-Platformz	"Windows"zSec-Ch-Ua-Platform-Versionz"7.0.0"zSec-Fetch-Dest�documentzSec-Fetch-Mode�navigatezSec-Fetch-Sitezsame-originzSec-Fetch-Userz?1zUpgrade-Insecure-Requestsz
User-AgentzoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36�cookie�returnc           	      �  � | t           d<   d}t          j        |t           ��  �        j        }t	          t          d� t          d|�  �        �  �        �  �        }g }|D ]t}	 t          j        |�  �        }||v r�n#  Y �!xY w|�                    dd�  �        r:|�                    dd�  �        r$|�	                    |d         |d         d	��  �         �u|S )
Nr   z3https://www.facebook.com/pages/?category=your_pages)�headersc                 �   � d| z   dz   S )N�{�}� )�ss    �tool_export_pagecookie.py�<lambda>zget_page_ids.<locals>.<lambda>!   s   � �#�a�%��)� �    z""profile":{(.*?),"profile_picture"�idF�name)r   r   )
r   �requests�get�text�list�mapr   �json�loads�append)r   �url�content�all_profile�res�profile�dict_profiles          r   �get_page_idsr)      s�   � ��G�H��
?�C��l�3�w�/�/�/�4�G��s�#�#��=�g�F�F�� � � �K� �C�� N� N��	� $�
�7� 3� 3�L��s�"�"�8�"���x�x�������D��'�'� 	N�L�,<�,<�V�E�,J�,J� 	N��J�J�\�$�/�|�F�7K�L�L�M�M�M���Js   � A:�:A>c                 �   � 	 t          d| �  �        d         }|S # t          $ r}t          d�  �         Y d }~dS d }~ww xY w)Nzc_user=(.*?);r   z[ERR] : can not find id� )r   �	Exception�print)r   �ID�BUGs      r   �get_user_id_from_cookier0   0   s\   � ���)�&�1�1�!�4���	��� � � ��'�(�(�(��r�r�r�r�r��������s   � �
>�9�>�pageIdc                 �P   � t          | �  �        }| �                    ||�  �        }|S )zcparameters : cookie

                    pageId (get list of pageId by using get_page_ids function))r0   �replace)r   r1   r.   �
new_cookies       r   �get_page_cookier5   9   s*   � � 
!��	(�	(�B�����6�*�*�J��r   �	page_info�page_cookiec                 �|   � t          dd�  �        }t          d| d         |��  �         t          d||d��  �         d S )	N�cookies_out.txt�azNAME :r   )�filezCOOKIE:z


)r;   �end)�openr-   )r6   r7   �
file_writes      r   �
write_datar?   @   sI   � ��'��,�,�J�	�(�9�V�$�:�6�6�6�6�	�)�K�Z�H�=�=�=�=�=�=r   uE    [lưu ý]: mỗi cookie trong file được ngăn cách nhau 1 dòngu%   nhập đường dẫn tệp cookie :�rc                 �*   � | �                     �   �         S )N)�strip)�vals    r   r   r   K   s   � �s�y�y�{�{� r   u/   nhập số lượng luồng : [recommended 3] c                 �,   � g | ]}t          |�  �        ��S r   )r)   )�.0r   s     r   �
<listcomp>rF   N   s    � �C�C�C�V�L��(�(�C�C�Cr   r9   �wr+   r   )�target�argsT�Doneu   ấn enter để thoát >>)&r   r    �	threading�collectionsr   �rer   �strr   r   �dictr)   r0   r5   r?   r-   �input�	file_pathr=   r;   r   �	readlines�cookie_list�int�
num_thread�
page_infos�cookies�write�range�_�popr6   r   �data�Thread�thread�daemon�startr   r   r   �<module>ra      s�  �� ���� ���� � � � � � � � � � � � � � � � ���"���  W�� �d�� �K�	�
 �S�� 
�#�� �R�� "�  #A�� �t�� �d�� ��� !��� �Z�� �Z�� �]��  �T�!�"  ��#�$ �  C�%� ��*�� �t�D��S��M�2� � � � �(�3� �#� � � � ��3� �c� �S� � � � �>�� >�#� >� >� >� >� ��M� N� N� N��E�9�:�:�	�	�T�)�C��� F�D��$�s�s�2�2�4�>�>�3C�3C�D�D�E�E�K�F� F� F� F� F� F� F� F� F� F� F���� F� F� F� F� �S���H�I�I�J�J�
��U�C�C�{�C�C�C�D�D�
�
�%��
�
��	�T�
�C� � � 7�D����B���� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7���� 7� 7� 7� 7�	��z�	�	� � �A���� � �I��[�[�]�]�F�� � ��!��!�*�D���QW�X\�]a�Xb�Ac�Ac�;e�f�f�f�������������
 ��f���� ��"� #� #� #� #� #s$   �$)C�C� C�$E�E
�E
