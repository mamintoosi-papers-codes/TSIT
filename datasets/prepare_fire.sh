#!/usr/bin/env bash
فعلا کاری بهش ندارم
set -x

DATAROOT=$1

cp -r ./datasets/fire_lists $DATAROOT
ln -s $DATAROOT ./datasets
