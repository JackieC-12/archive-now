// Action Types
const LOAD_ARCHIVES = 'archives/LOAD_ARCHIVES'
const ADD_ARCHIVE = 'archives/ADD_ARCHIVE'

// Action Creators
const loadArchives = (archives) => ({
    type: LOAD_ARCHIVES,
    archives
})

const addArchive = (archive) => ({
    type: ADD_ARCHIVE,
    archive
})

//
export const fetchArchives = () => async (dispatch) => {
    const response = await fetch('/api/archvies')
    if (response.ok) {
        const data = await response.json();

        console.log("Fetched archives data:", data)

        if (Array.isArray(data.Archives)) {
            dispatch(loadArchives(data.Archives))
        } else {
            console.error("Archive data is not in the expected array format:", data.Archives)
        }
    }

    else {
        console.error("Failed to fetch Archives")
    }
}


export const createArchive = (payload) => async (dispatch) => {
    const { url, title, description } = payload;

    console.log("Creating Archive with Data:", { url, title, description})

    const response = await fetch("/api/archives/new", {
        method: "POST",
        headers: { "Content-Type": "application/json" } ,
        body: JSON.stringify(user)
    })

    // if (!response.ok) {
    //     const errorData = await response.json();
    //     console.error("Error Data:", errorData);
    //     throw new Error("Failed to create archive")
    // }

    const newArchive = await response.json();
    dispatch(addArchive(newArchive))
    return newSpot
}

// Initial State
const initialState = {
    Archives: {}
}

// Reducer
export default function archiveReducer(state = initialState, action) {
    switch (action.type) {
        // case LOAD_ARCHIVES
        case LOAD_ARCHIVES: {
            const newState = { ...state, Archives: {} };
            action.archives.forEach((archive) => {
                newState.Archives[archive.id] = archive
            })

            return newState
        }

        // case SET_USER_ARCHIVES

        case ADD_ARCHIVE: {
            return {
                ...state,
                Archives: {
                    ...state.Archives,
                    [action.archive.id]: action.archive,
                },
                UserArchives: {
                    ...state.UserArchives,
                    [action.archive.id]: action.archive
                }
            }
        }

        // case UPDATE_ARCHIVE
        // case DELETE_ARCHIVE
    }
}
