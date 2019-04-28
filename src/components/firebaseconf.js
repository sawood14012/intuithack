import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/database';
import 'firebase/auth';

const config = {
  apiKey: 'AIzaSyC-au5_fVv-Md0W_lw_w2eQl9DRF_itvOc',
  authDomain: 'intuithack-d1be6.firebaseapp.com',
  databaseURL: 'https://intuithack-d1be6.firebaseio.com',
  projectId: 'intuithack-d1be6',
  storageBucket: 'intuithack-d1be6.appspot.com',
  messagingSenderId: '70649152783',
};

firebase.initializeApp(config);

const db = firebase.firestore();
const auth = firebase.auth();
const user = auth.currentUser;
// const currentUser = auth.currentUser
const rdb = firebase.database();
const r = firebase.database();
const settings = {
  timestampsInSnapshots: true,
};
db.settings(settings);

export {
  db,
  user,
  r,
  rdb,
  auth,
};
