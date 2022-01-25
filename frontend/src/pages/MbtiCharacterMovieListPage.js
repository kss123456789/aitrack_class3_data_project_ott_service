import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import prevbtn from "../img/prevbtn.png";
import home from "../img/home.png";
import MovieInfoModal from "../components/MovieInfoModal";
import styles from "./MbtiCharacterMovieListPage.module.css";


const MbtiCharacterMovieListPage = () => {
    const [userMBTI, setUserMBTI] = useState("");
    const [movieList, setMovieList] = useState([]);
    const [selectedMovie, setSelectedMovie] = useState([]);

    const [showModal, setShowModal] = useState(false);

    const history = useHistory();

    const openModal = () => {
        setShowModal(!showModal);
    }

    useEffect(() => {
        async function getMbti() {
            try {
                const mbti = await axios.get("http://localhost:5000/result/", {withCredentials: true})
                setUserMBTI(mbti.data.user_mbti)
            } catch (error) {
                console.log(error)
            }
        }
        getMbti();
    }, [userMBTI]);

    useEffect(() => {
        async function getMbtiCharacterMovieList() {
            try {
                const res = await axios.get(`http://localhost:5000/character/movie_list/${userMBTI}/0`, {withCredentials: true})
                setMovieList(res.data.total_character_N_movies)
            } catch (error) {
                console.log(error)
            }
        }
        getMbtiCharacterMovieList();
    }, [userMBTI]);

    const clickHandler = (item) => {
        setSelectedMovie(item);
        openModal();
    }
    
    const logout = () => {
        axios
            .get("http://localhost:5000/user/logout", {withCredentials: true})
            .then(() => {
                history.push("/")
            })
            .catch((error) => {
                console.log(error)
            })
    }
    
    return (
        <div id={styles.container}>
            <div id={styles.btnbox} onClick={  () => { history.goBack() } }>
                <img className={styles.prevbtn} src={ prevbtn } alt="prevbtn" />
            </div>

            <div className={styles.title}>
                <p>일리스</p>
            </div>

            <div id={styles.divider}></div>

            <div>
                { movieList && movieList.map((items, idx) => {
                    return (
                        <div>
                            <div>
                                <p className={styles.char_name} key={ idx }>{ items.character_name + " 등장한 영화" } </p>
                            </div>
                        <div className={styles.charlist}>
                            { items.movies.map((item, idx) => {
                                return (
                                    <div>
                                        <img className={styles.char_img} key={ idx } src={ item.image_link } alt={ item.kor_title + " 포스터" } onClick={ () => clickHandler(item) } />
                                        <p className={styles.movie_name}>{ item.kor_title }</p>
                                        { showModal && <MovieInfoModal openModal={openModal} movieList={movieList} selectedMovie={selectedMovie} />}
                                    </div>
                                )
                            }) }
                        </div>
                    </div>
                    )
                }) }
                
                <div>
                    <img className={styles.homebtn} src={ home } alt="home button" onClick={ logout } />
                </div>
            </div>

        </div>
    )
}

export default MbtiCharacterMovieListPage;